# Copyright Mission 42 Ventures, Inc. All rights reserved.
# Unauthorized copying, distribution, or use is prohibited.

class_name WorkspaceSchema extends Node

static var J := JSONSchema

# ============================================================================
# WORKSPACE
# ============================================================================

static func create_schema() -> JSONSchema.BaseSchema:
	var my_validator := J.object({
		"tangibles": J.array(J.one_of([
			fraction_shape(),
			vocab(),
			num_line(),
			benchmark()
		])),
		"shuffle_tangibles": J.boolean().optional()
	}).type(WorkspaceData)

	my_validator.serializer(func(workspace_data: WorkspaceData) -> Dictionary:
		var result := { }

		result["tangibles"] = workspace_data.tangibles

		if workspace_data.shuffle_tangibles:
			result["shuffle_tangibles"] = true

		return result
	)

	return my_validator

# ============================================================================
# TANGIBLES
# ============================================================================

static var TYPE_FRACTION_SHAPE: String = "fraction_shape"
static var TYPE_NUMBER_LINE: String = "number_line"
static var TYPE_VOCAB: String = "vocab"
static var TYPE_NUM_LINE: String = "num_line"

## Maps a [code]Visual[/code] to its [String] representation.
const VISUAL_TO_STRING = {
	NumLine.Visual.BAR: "bar",
	NumLine.Visual.PIE: "pie",
	NumLine.Visual.GRID: "grid",
	NumLine.Visual.EQUATION: "equation",
	NumLine.Visual.BAR_SM: "bar_sm",
	NumLine.Visual.COMPOSITE_BAR_EQUATION: "composite_bar_equation",
	NumLine.Visual.LINE: "line",
	NumLine.Visual.POLYGON: "polygon"
}

## Maps a [String] to its [code]Visual[/code] representation.
const STRING_TO_VISUAL = {
	"bar": NumLine.Visual.BAR,
	"pie": NumLine.Visual.PIE,
	"grid": NumLine.Visual.GRID,
	"equation": NumLine.Visual.EQUATION,
	"bar_sm": NumLine.Visual.BAR_SM,
	"composite_bar_equation": NumLine.Visual.COMPOSITE_BAR_EQUATION,
	"line": NumLine.Visual.LINE,
	"polygon": NumLine.Visual.POLYGON
}

static func tangible() -> JSONSchema.BaseSchema:
	return J.object({
		"@col": J.integer().optional(),
		"@layout": J.string().one_of(["underlay", "default", "overlay"]).optional(),
		"is_visible": J.boolean().optional()
	})

static func fraction() -> JSONSchema.BaseSchema:
	var schema = J.string()
	#var schema = J.one_of([J.string().pattern(r"^[0-9]+/[0-9]+$"), J.string().pattern(r"^[0-9]+$")])

	schema.deserializer(func(value: String) -> Fraction:
		var parts = value.split("/")
		var numerator = int(parts[0])
		var denominator = int(parts[1]) if parts.size() > 1 else 1
		return Fraction.new(numerator, denominator)
	)

	schema.serializer(func(value: Fraction) -> Variant:
		return "%d" % [value.numerator] if value.denominator == 1 else "%d/%d" % [value.numerator, value.denominator]
	)

	return schema

static func fraction_shape() -> JSONSchema.BaseSchema:
	var schema = tangible().extend({
		# if string, then it's a uniform bar
		# if null, then it is a whole bar
		"fractions": J.one_of([J.array(fraction()), fraction()]).optional(),
		"visual": J.integer().optional(),
		# indexes of shaded fractions
		"shaded": J.array(J.integer()).optional(),
		"missing": J.array(J.integer()).optional(),
		"frac_label_visible": J.array(J.integer()).optional(),
		"read_only_parts": J.array(J.integer()).optional(),
		"lcm": J.integer().optional(),
		"num_rows": J.integer().optional(),
		"is_read_only": J.boolean().optional(),
		"is_visible": J.boolean().optional(),
		"sum_is_visible": J.boolean().optional()
	}).type(FracShape)

	schema.deserializer(func(value: Dictionary):
		var new_num_line := NumLine.new()

		## Sum visibility
		new_num_line._sum._is_visible = value.get("sum_is_visible", false)

		## LCM
		new_num_line._lcm = value.get("lcm", 24)

		## Visual
		new_num_line._visual = value.get("visual", NumLine.Visual.BAR)
		if new_num_line._visual == NumLine.Visual.GRID:
			return JSONSchema.ValidationError.new("visual", "Fraction shapes of type 'GRID' (%d) are deprecated and should not be used." % NumLine.Visual.GRID)

		## Visibility
		new_num_line._is_visible = value.get("is_visible", true)

		## Read only
		new_num_line.is_read_only = value.get("is_read_only", false)

		## Range
		var range_array = [0, 1]
		var start: int = range_array[0]
		var end: int = range_array[1]
		new_num_line._range = Vector2i(start, end)

		## Ticks/intervals
		var ticks = []
		var intervals = value.get("fractions", [Fraction.new(1, 1)])

		if intervals is Fraction:
			ticks = intervals
		else:
			var tick = Vector2i(0, 1)
			ticks = [Fraction.new(tick.x, tick.y)]

			for interval in intervals:
				tick = FracUtils.add(tick.x, tick.y, interval.numerator, interval.denominator)
				ticks.append(Fraction.new(tick.x, tick.y))

		if ticks is Fraction:
			var interval: Fraction = ticks
			ticks = []
			var numerator = start * interval.denominator
			var denominator = interval.denominator
			while numerator <= end * interval.denominator:
				##Accounts for case where ticks is ""
				if interval.numerator == 0:
					ticks = [Fraction.new(start, 1), Fraction.new(end, 1)]
					break
				if numerator % denominator == 0:
					@warning_ignore("integer_division")
					ticks.append(Fraction.new(numerator / denominator, 1))
				else:
					ticks.append(Fraction.new(numerator, denominator))
				numerator += interval.numerator

		for tick in ticks:
			new_num_line.insert_tick(tick)

		## Tick frac labels
		var labels = value.get("labels", true)
		if labels is bool:
			if labels:
				for tick in new_num_line._ticks.values():
					tick.frac_label = Vector2i(tick.numerator, tick.denominator)
					tick.is_frac_label_visible = true
		elif labels is Array:
			for frac in labels:
				var tick = new_num_line.get_tick(frac.numerator, frac.denominator)
				if tick:
					tick.frac_label = Vector2i(frac.numerator, frac.denominator)
					tick.is_frac_label_visible = true
				else:
					# TODO EDTECH-3768: This should really be a validation "warning" with JSON path information.
					push_warning("Tick is null.")

		## Interval frac labels
		var intervals_is_frac_label_visible = value.get("frac_label_visible", false)
		if intervals_is_frac_label_visible is bool:
			if intervals_is_frac_label_visible:
				for interval in new_num_line._intervals:
					interval.frac_label = Vector2i(interval.numerator, interval.denominator)
					interval.is_frac_label_visible = true
		elif intervals_is_frac_label_visible is Array:
			for i in intervals_is_frac_label_visible:
				var interval = new_num_line._intervals[i]
				interval.frac_label = Vector2i(interval.numerator, interval.denominator)
				interval.is_frac_label_visible = true

		## Shaded intervals
		var intervals_is_shaded = value.get("shaded", false)
		if intervals_is_shaded is bool:
			if intervals_is_shaded:
				for interval in new_num_line._intervals:
					interval.is_shaded = true
		elif intervals_is_shaded is Array:
			for index in intervals_is_shaded:
				new_num_line._intervals[index].is_shaded = true

		## Read only ticks
		var ticks_is_read_only = value.get("ticks_is_read_only", false)
		if ticks_is_read_only is bool:
			if ticks_is_read_only:
				for tick in new_num_line._ticks.values():
					tick.is_read_only = true
		elif ticks_is_read_only is Array:
			for frac in ticks_is_read_only:
				var tick = new_num_line.get_tick(frac.numerator, frac.denominator)
				tick.is_read_only = true

		## Read only intervals
		var intervals_is_read_only = value.get("read_only_parts", false)
		if intervals_is_read_only is bool:
			if intervals_is_read_only:
				for interval in new_num_line._intervals:
					interval.is_read_only = true
		elif intervals_is_read_only is Array:
			for index in intervals_is_read_only:
				new_num_line._intervals[index].is_read_only = true

		return new_num_line
	)

	return schema

static func vocab() -> JSONSchema.BaseSchema:
	var schema = tangible().extend({
		"label": J.string(),
		"is_visible": J.boolean().optional(),
		"is_highlighted": J.boolean().optional()
	}).type(Vocab)

	schema.deserializer(func(value: Dictionary) -> Variant:
		var label = value.get("label", "")
		var is_visible = value.get("is_visible", true)
		var is_highlighted = value.get("is_highlighted", false)
		var new_vocab = Vocab.new(label, is_visible, is_highlighted)
		new_vocab.col = value.get("@col", 0)
		new_vocab.layout = value.get("@layout", "default")
		return new_vocab
	)

	schema.serializer(func(value: Vocab) -> Variant:
		var result: Dictionary = {}
		result["label"] = value.label
		result["is_visible"] = value._is_visible
		result["is_highlighted"] = value.is_highlighted
		if value.col:
			result["@col"] = value.col
		if value.layout != "default":
			result["@layout"] = value.layout
		return result
	)

	return schema

static func benchmark() -> JSONSchema.BaseSchema:
	var schema = tangible().extend({
		"location": fraction().optional()
	}).type(Benchmark)

	schema.deserializer(func(value: Dictionary) -> Benchmark:
		var new_benchmark = Benchmark.new()
		new_benchmark.location = value.get("location", Fraction.new(1,2))
		new_benchmark.location.is_frac_label_visible = true
		new_benchmark.col = value.get("@col", 0)
		new_benchmark.layout = value.get("@layout", "underlay")
		return new_benchmark
	)

	schema.serializer(func(value: Benchmark) -> Dictionary:
		var result: Dictionary = {}
		if Vector2i(value.location.numerator, value.location.denominator) != Vector2i(1, 2):
			result["location"] = value.location
		if value.col:
			result["@col"] = value.col
		if value.layout != "underlay":
			result["@layout"] = value.layout
		return result
	)

	return schema

static func num_line() -> JSONSchema.BaseSchema:
	var schema = tangible().extend({
		"visual": J.one_of([J.integer(), J.string()]).optional(),
		"sum_is_visible": J.boolean().optional(),
		"intervals_is_shaded": J.one_of([J.boolean(), J.array(J.integer())]).optional(),
		"lcm": J.integer().optional(),
		"range": J.array(J.integer()).optional(),
		"ticks": J.one_of([J.array(fraction()), fraction()]).optional(),
		"intervals": J.one_of([J.array(fraction()), fraction()]).optional(),
		"points": J.array(fraction()).optional(),
		"labels": J.one_of([J.boolean(), J.array(fraction())]).optional(),
		"alt_labels": J.one_of([J.boolean(), J.array(fraction())]).optional(),
		"invert_labels": J.boolean().optional(),
		"intervals_is_frac_label_visible": J.one_of([J.boolean(), J.array(J.integer())]).optional(),
		"ticks_is_read_only": J.one_of([J.boolean(), J.array(fraction())]).optional(),
		"is_read_only": J.boolean().optional()
	}).type(NumLine)

	schema.deserializer(func(value: Dictionary):
		var new_num_line := NumLine.new()

		# Layout
		new_num_line.col = value.get("@col", 0)
		new_num_line.layout = value.get("@layout", "default")

		## Sum visibility
		new_num_line._sum._is_visible = value.get("sum_is_visible", false)

		## LCM
		new_num_line._lcm = value.get("lcm", 24)

		## Visual
		var visual = value.get("visual", NumLine.Visual.LINE)
		if visual is String:
			var visual_str = visual
			visual = STRING_TO_VISUAL.get(visual)
			if visual == null:
				return JSONSchema.ValidationError.new("visual", "Unsupported visual '%s'" % visual_str)
		new_num_line._visual = visual
		if new_num_line._visual == NumLine.Visual.GRID:
			return JSONSchema.ValidationError.new("visual", "Number lines of type 'GRID' (%d) are deprecated and should not be used." % NumLine.Visual.GRID)

		## Visibility
		new_num_line._is_visible = value.get("is_visible", true)

		## Read only
		new_num_line.is_read_only = value.get("is_read_only", false)

		## Range
		var range_array = value.get("range", [0, 1])
		var start: int = range_array[0]
		var end: int = range_array[1]
		new_num_line._range = Vector2i(start, end)

		## Ticks/intervals
		var ticks = value.get("ticks", [])
		var intervals = value.get("intervals", [])

		if ticks and intervals:
			JSONSchema.ValidationError.new("intervals", "Ticks and intervals cannot both be set.")
		elif not ticks and not intervals:
			ticks = [Fraction.new(start, 1), Fraction.new(end, 1)]
		elif not ticks and intervals:
			if intervals is Fraction:
				ticks = intervals
			else:
				var tick = Vector2i(start, 1)
				ticks = [Fraction.new(tick.x, tick.y)]
				for interval in intervals:
					if interval.numerator == 0 or interval.denominator == 0:
						continue
					tick = FracUtils.add(tick.x, tick.y, interval.numerator, interval.denominator)
					ticks.append(Fraction.new(tick.x, tick.y))

		if ticks is Fraction:
			var interval: Fraction = ticks
			ticks = []
			var numerator = start * interval.denominator
			var denominator = interval.denominator
			while numerator <= end * interval.denominator:
				##Accounts for case where ticks is "" or "1/"
				if interval.numerator == 0 or interval.denominator == 0:
					ticks = [Fraction.new(start, 1), Fraction.new(end, 1)]
					break
				if numerator % denominator == 0:
					@warning_ignore("integer_division")
					ticks.append(Fraction.new(numerator / denominator, 1))
				else:
					ticks.append(Fraction.new(numerator, denominator))
				numerator += interval.numerator

		for tick in ticks:
			new_num_line.insert_tick(tick)

		## Points
		for point in value.get("points", []):
			new_num_line.insert_point(point)

		## Tick frac labels
		var labels = value.get("labels", true)
		if labels is bool:
			if labels:
				for tick in new_num_line._ticks.values():
					tick.frac_label = Vector2i(tick.numerator, tick.denominator)
					tick.is_frac_label_visible = true
		elif labels is Array:
			for frac in labels:
				var tick = new_num_line.get_tick(frac.numerator, frac.denominator)
				tick.frac_label = Vector2i(frac.numerator, frac.denominator)
				tick.is_frac_label_visible = true

		# ALT LABELS
		var alt_labels = value.get("alt_labels", false)
		if alt_labels is bool:
			if alt_labels:
				for tick in new_num_line._ticks.values():
					tick.alt_frac_label = Vector2i(tick.numerator, tick.denominator)
					tick.is_alt_frac_label_visible = true
		elif alt_labels is Array:
			for frac in alt_labels:
				var tick = new_num_line.get_tick(frac.numerator, frac.denominator)
				tick.alt_frac_label = Vector2i(frac.numerator, frac.denominator)
				tick.is_alt_frac_label_visible = true

		## Interval frac labels
		var intervals_is_frac_label_visible = value.get("intervals_is_frac_label_visible", false)
		if intervals_is_frac_label_visible is bool:
			if intervals_is_frac_label_visible:
				for interval in new_num_line._intervals:
					interval.frac_label = Vector2i(interval.numerator, interval.denominator)
					interval.is_frac_label_visible = true
		elif intervals_is_frac_label_visible is Array:
			for index in intervals_is_frac_label_visible:
				var interval = new_num_line._intervals[index]
				interval.frac_label = Vector2i(interval.numerator, interval.denominator)
				interval.is_frac_label_visible = true

		# INVERT LABELS
		new_num_line.invert_labels = value.get("invert_labels", false)

		## Shaded intervals
		var intervals_is_shaded = value.get("intervals_is_shaded", false)
		if intervals_is_shaded is bool:
			if intervals_is_shaded:
				for interval in new_num_line._intervals:
					interval.is_shaded = true
		elif intervals_is_shaded is Array:
			for index in intervals_is_shaded:
				new_num_line._intervals[index].is_shaded = true

		## Read only ticks
		var ticks_is_read_only = value.get("ticks_is_read_only", false)
		if ticks_is_read_only is bool:
			if ticks_is_read_only:
				for tick in new_num_line._ticks.values():
					tick.is_read_only = true
		elif ticks_is_read_only is Array:
			for frac in ticks_is_read_only:
				if frac.denominator == 0:
					continue
				var tick = new_num_line.get_tick(frac.numerator, frac.denominator)
				tick.is_read_only = true

		## Read only intervals
		var intervals_is_read_only = value.get("intervals_is_read_only", false)
		if intervals_is_read_only is bool:
			if intervals_is_read_only:
				for interval in new_num_line._intervals:
					interval.is_read_only = true
		elif intervals_is_read_only is Array:
			for index in intervals_is_read_only:
				new_num_line._intervals[index].is_read_only = true

		return new_num_line
	)

	schema.serializer(func(value: NumLine) -> Variant:
		var result: Dictionary = {}

		if value.col:
			result["@col"] = value.col
		if value.layout != "default":
			result["@layout"] = value.layout

		## Sum visibility
		if value._sum._is_visible:
			result["sum_is_visible"] = true

		## LCM
		if value._lcm != 24:
			result["lcm"] = value._lcm

		## Visual
		if value._visual != NumLine.Visual.LINE:
			result["visual"] = VISUAL_TO_STRING[value._visual]

		## Visibility
		if not value._is_visible:
			result["is_visible"] = false

		## Read only
		if value.is_read_only:
			result["is_read_only"] = true

		## Range
		if value._range != Vector2i(0, 1):
			result["range"] = [value._range.x, value._range.y]

		## Ticks/intervals
		var ticks = value.get_ticks()
		var difference = FracUtils.subtract(ticks[1].numerator, ticks[1].denominator, ticks[0].numerator, ticks[0].denominator)
		var first_interval = FracUtils.reduce(difference.x, difference.y)
		var is_uniform = true
		for i in range(1, ticks.size()):
			difference = FracUtils.subtract(ticks[i].numerator, ticks[i].denominator, ticks[i - 1].numerator, ticks[i - 1].denominator)
			var interval = FracUtils.reduce(difference.x, difference.y)
			if first_interval != interval:
				is_uniform = false

		# If the start or end tick is not present, we cannot use single fraction shorthand.
		if Vector2i(ticks[0].numerator, ticks[0].denominator) != Vector2i(value._range.x, 1) or Vector2i(ticks[-1].numerator, ticks[-1].denominator) != Vector2i(value._range.y, 1):
			is_uniform = false

		if is_uniform:
			if first_interval != Vector2i(1, 1):
				if value._visual == NumLine.Visual.LINE:
					result["ticks"] = Fraction.new(first_interval.x, first_interval.y)
				else:
					result["intervals"] = Fraction.new(first_interval.x, first_interval.y)
		else:
			if value._visual == NumLine.Visual.LINE:
				result["ticks"] = ticks
			else:
				result["intervals"] = value._intervals

		## Points
		var points := value._points.values()
		if points:
			result["points"] = points

		## Tick frac labels
		var labels = []
		var all_labeled = true
		var all_not_labeled = true
		for frac in value._ticks.values():
			if frac.is_frac_label_visible:
				all_not_labeled = false
				labels.append(Fraction.new(frac.frac_label.x, frac.frac_label.y))
			else:
				all_labeled = false
		if not all_labeled:
			if all_not_labeled:
				result["labels"] = false
			else:
				result["labels"] = labels

		# ALT LABELS
		var alt_labels = []
		all_labeled = true
		all_not_labeled = true
		for frac in value._ticks.values():
			if frac.is_alt_frac_label_visible:
				all_not_labeled = false
				alt_labels.append(Fraction.new(frac.alt_frac_label.x, frac.alt_frac_label.y))
			else:
				all_labeled = false
		if not all_not_labeled:
			if all_labeled:
				result["alt_labels"] = true
			else:
				result["alt_labels"] = alt_labels

		## Interval frac labels
		var intervals_is_frac_label_visible = []
		var all_intervals_is_frac_label_visible = true
		var all_not_intervals_is_frac_label_visible = true
		for index in range(value._intervals.size()):
			var interval = value._intervals[index]
			if interval.is_frac_label_visible:
				all_not_intervals_is_frac_label_visible = false
				intervals_is_frac_label_visible.append(index)
			else:
				all_intervals_is_frac_label_visible = false
		if not all_not_intervals_is_frac_label_visible:
			if all_intervals_is_frac_label_visible:
				result["intervals_is_frac_label_visible"] = true
			else:
				result["intervals_is_frac_label_visible"] = intervals_is_frac_label_visible

		# INVERT LABELS
		if value.invert_labels:
			result["invert_labels"] = true

		## Read only ticks
		var ticks_is_read_only = []
		var all_ticks_is_read_only = true
		var all_ticks_not_is_read_only = true
		for frac in value._ticks.values():
			if frac.is_read_only:
				all_ticks_not_is_read_only = false
				ticks_is_read_only.append(Fraction.new(frac.numerator, frac.denominator))
			else:
				all_ticks_is_read_only = false
		if not all_ticks_not_is_read_only:
			if all_ticks_is_read_only:
				result["ticks_is_read_only"] = true
			else:
				result["ticks_is_read_only"] = ticks_is_read_only

		## Read only intervals
		var intervals_is_read_only = []
		var all_intervals_is_read_only = true
		var all_intervals_not_is_read_only = true
		for index in range(value._intervals.size()):
			var interval = value._intervals[index]
			if interval.is_read_only:
				all_intervals_not_is_read_only = false
				intervals_is_read_only.append(index)
			else:
				all_intervals_is_read_only = false
		if not all_intervals_not_is_read_only:
			if all_intervals_is_read_only:
				result["intervals_is_read_only"] = true
			else:
				result["intervals_is_read_only"] = intervals_is_read_only

		## Shaded intervals
		var intervals_is_shaded = []
		var all_is_shaded = true
		var all_not_is_shaded = true
		for i in range(value._intervals.size()):
			var interval = value._intervals[i]
			if interval.is_shaded:
				all_not_is_shaded = false
				intervals_is_shaded.append(i)
			else:
				all_is_shaded = false
		if not all_not_is_shaded:
			if all_is_shaded:
				result["intervals_is_shaded"] = true
			else:
				result["intervals_is_shaded"] = intervals_is_shaded

		return result
	)

	return schema
