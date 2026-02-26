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
			cut_grid(),
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
				"move":
					result = Move.new(&"points")
					result.palette = Palette.new(&"points", [PointStack.new(null, -1)])
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
	var schema := J.object({
		"mode": J.string().optional(),
		"allow_multiple": J.boolean().optional(),
		"palette": PaletteSchema.create_schema().optional(),
	}).type(Move)

	schema.deserializer(func(value : Dictionary) -> Move:
		var model := Move.new()

		var mode := value.get("mode", "") as StringName
		var palette := value.get("palette", null) as Palette

		if mode.is_empty():
			# HACK: Default to Fraction labels or Points mode depending on whether a Palette is present.
			if palette:
				mode = &"frac_labels"
			else:
				# HACK: Give Points mode a non-empty Palette by default so that we display the UI.
				mode = &"points"
				palette = Palette.new(&"points", [PointStack.new(null, -1)])

		model.mode = mode
		model.allow_multiple = value.get("allow_multiple", true)
		model.palette = palette

		return model
	)

	schema.serializer(func(model : Move) -> Dictionary:
		# NOTE: In the near future, JSON deserialization will fail if the mode is NOT present on Move.
		assert(not model.mode.is_empty(), "Mode is required")

		var value := {
			"mode" : model.mode as String,
		}

		if not model.allow_multiple:
			value["allow_multiple"] = false

		if model.palette:
			value["palette"] = model.palette

		return value
	)

	return schema

static func drag() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"lcm": J.integer().optional(),
		"palette": PaletteSchema.create_schema().optional(),
		"labels": J.array(WorkspaceSchema.fraction()).optional(),
		"quantities": J.array(J.integer()).optional(),
	}).type(Drag)

	schema.deserializer(func(value: Dictionary) -> Variant:
		# Replace the Drag tool in content with a Fraction label Move tool.
		var move_tool := Move.new()
		move_tool.mode = &"frac_labels"

		var palette = value.get("palette")
		if palette:
			if not palette is Palette:
				return JSONSchema.ValidationError.new("palette", "Must be an object of type Palette")

			move_tool.palette = palette
			return move_tool

		# LEGACY: Migrate the old "labels" and "quantities" properties on Drag into the new Palette representation.
		var labels : Array[Fraction] = []
		labels.assign(value.get("labels", []))

		if labels.size() == 0:
			# No labels were specified, so ignore the legacy data.
			return move_tool

		var quantities : Array[int] = []
		quantities.assign(value.get("quantities", []))

		move_tool.palette = PaletteSchema.create_palette_with_frac_labels(labels, quantities)
		return move_tool
	)

	return schema

static func cut_grid() -> JSONSchema.BaseSchema:
	return J.object({}).type(CutGrid)
