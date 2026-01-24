class_name ToolSchema extends Node

static var J := JSONSchema

static func create_schema() -> JSONSchema.BaseSchema:
	var schema = J.one_of(
		[
			cut(),
			paint(),
			select(),
			comp_frame(),
			highlight(),
			place(),
			drag(),
			move(),
			J.string().one_of([
				"cut",
				"paint",
				"single_paint",
				"select",
				"multi_select",
				"comp_frame",
				"highlight",
				"move"
			])
		]
	)

	## Backwards compatibility
	schema.deserializer(func(value: Variant) -> Tool:
		if value is String:
			var result
			match value:
				"cut": result = Place.new()
				"paint": result = Paint.new()
				"single_paint": result = Paint.new(false)
				"select": result = Select.new()
				"multi_select":
					result = Select.new()
					result.is_single = false
				"comp_frame": result = CompFrame.new()
				"highlight": result = Highlight.new()
				"move": result = Move.new()
			return result
		return value
	)

	return schema

static func cut() -> JSONSchema.BaseSchema:
	var schema = J.object({}).type(Cut)

	schema.deserializer(func(_value: Dictionary) -> Place:return Place.new())

	return schema

static func paint() -> JSONSchema.BaseSchema:
	return J.object({
		"is_single": J.boolean().optional()
	}).type(Paint)

static func select() -> JSONSchema.BaseSchema:
	return J.object({
		"is_single": J.boolean().optional()
	}).type(Select)

static func comp_frame() -> JSONSchema.BaseSchema:
	return J.object({}).type(CompFrame)

static func highlight() -> JSONSchema.BaseSchema:
	return J.object({}).type(Highlight)

static func place() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"lcm": J.integer().optional(),
		"is_single": J.boolean().optional(),
		"bounds": J.array(WorkspaceSchema.fraction()).optional()
	}).type(Place)

	schema.deserializer(func(value: Dictionary) -> Place:
		var new_place = Place.new()
		new_place.lcm = value.get("lcm", 0)
		new_place.is_single = value.get("is_single", false)
		var bounds = value.get("bounds", [])
		if bounds:
			var lower_bound: int = bounds[0].numerator * new_place.lcm / bounds[0].denominator
			var upper_bound: int = bounds[1].numerator * new_place.lcm / bounds[1].denominator
			new_place.bounds = [lower_bound, upper_bound]
		return new_place
	)

	schema.serializer(func(value: Place) -> Dictionary:
		var result: Dictionary = {}
		if value.lcm != 0:
			result["lcm"] = value.lcm
		if value.is_single:
			result["is_single"] = true
		if value.bounds:
			var lower_bound := FracUtils.reduce(value.bounds[0], value.lcm)
			var upper_bound := FracUtils.reduce(value.bounds[1], value.lcm)
			result["bounds"] = [Fraction.new(lower_bound.x, lower_bound.y), Fraction.new(upper_bound.x, upper_bound.y)]
		return result
	)

	return schema

static func move() -> JSONSchema.BaseSchema:
	return J.object({
		"palette": SequenceSchema.palette().optional(),
	}).type(Move)

static func drag() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"lcm": J.integer().optional(),
		"palette": SequenceSchema.palette().optional(),
		"labels": J.array(WorkspaceSchema.fraction()).optional(),
		"quantities": J.array(J.integer()).optional(),
	}).type(Drag)

	schema.deserializer(func(value: Dictionary) -> Variant:
		var drag_tool := Drag.new()

		var palette = value.get("palette")
		if palette:
			if not palette is Palette:
				return JSONSchema.ValidationError.new("palette", "Must be an object of type Palette")

			drag_tool.palette = palette
			return drag_tool

		# LEGACY: Migrate the old "labels" and "quantities" properties on Drag into the new Palette representation.
		var labels : Array[Fraction] = []
		labels.assign(value.get("labels", []))

		if labels.size() == 0:
			# No labels were specified, so ignore the legacy data.
			return drag_tool

		var quantities : Array[int] = []
		quantities.assign(value.get("quantities", []))

		# Fill in '1' for any quantities that are NOT specified in JSON.
		for i in range(quantities.size(), labels.size()):
			quantities.append(1)

		drag_tool.palette = Palette.with_fractions(labels, quantities)
		return drag_tool
	)

	return schema
