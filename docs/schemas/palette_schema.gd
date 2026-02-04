@abstract class_name PaletteSchema

static var J := JSONSchema

static func create_schema() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"labels": J.array(WorkspaceSchema.fraction()).optional(),
		"quantities": J.array(J.integer()).optional(),
		"stacks": J.array(part_stack()).optional(),
	}).type(Palette)

	schema.deserializer(func(value: Dictionary) -> Palette:
		var labels : Array[Fraction]
		labels.assign(value.get("labels", []))

		var quantities : Array[int]
		quantities.assign(value.get("quantities", []))

		var palette := create_palette_with_frac_labels(labels, quantities)

		var stacks : Array[PartStack]
		stacks.assign(value.get("stacks", []))

		palette.append_stacks(stacks)

		return palette
	)

	schema.serializer(func(in_palette : Palette) -> Dictionary:
		return {
			"stacks": in_palette._stacks,
		}
	)

	return schema


## Creates a [Palette] from parallel [Array]s of [Fraction] labels and quantities.
static func create_palette_with_frac_labels(labels : Array[Fraction], quantities : Array[int] = []) -> Palette:
	var stacks : Array[PartStack] = []

	for label_index in range(labels.size()):
		# Migrate legacy Fraction labels and quantities information if it exists.
		var in_frac_label := labels[label_index].frac_label
		var quantity := quantities[label_index] if label_index < quantities.size() else 1

		# NOTE: Give the stack the same capacity as its quantity, as legacy stacks did not have capacity.
		var stack := FracLabelStack.new(in_frac_label, quantity, quantity)
		stacks.push_back(stack)

	return Palette.new(&"frac_labels", stacks)


static func part_stack() -> JSONSchema.UnionSchema:
	# Any object that can appear in a Palette should be included in the list below.
	return J.one_of([
		frac_label(),
		point(),
	])


static func frac_label() -> JSONSchema.ObjectSchema:
	var schema := part_stack_base().extend({
		"label": WorkspaceSchema.fraction(),
	}).type(FracLabelStack)

	schema.deserializer(func(value : Dictionary) -> FracLabelStack:
		var fraction := value.get("label", Fraction.new()) as Fraction
		var quantity := value.get("quantity", 1) as int
		var capacity := value.get("capacity", quantity) as int
		return FracLabelStack.new(fraction.frac_label, quantity, capacity)
	)

	schema.serializer(func(in_stack : FracLabelStack) -> Dictionary:
		var out_label := in_stack.label
		var value := {
			"label": Fraction.new(out_label.x, out_label.y),
		}

		if in_stack.quantity != 1:
			value["quantity"] = in_stack.quantity

		if in_stack.capacity != in_stack.quantity:
			value["capacity"] = in_stack.capacity

		return value
	)

	return schema


static func point() -> JSONSchema.ObjectSchema:
	var schema := part_stack_base().type(PointStack)

	schema.deserializer(func(value : Dictionary) -> PointStack:
		var quantity := value.get("quantity", -1) as int
		var capacity := value.get("capacity", -1) as int
		return PointStack.new(null, quantity, capacity)
	)

	schema.serializer(func(in_stack : PointStack) -> Dictionary:
		var value := { }

		if in_stack.quantity != -1:
			value["quantity"] = in_stack.quantity

		if in_stack.capacity != -1:
			value["capacity"] = in_stack.capacity

		return value
	)

	return schema


static func part_stack_base() -> JSONSchema.ObjectSchema:
	return J.object({
		"quantity": J.integer().optional(),
		"capacity": J.integer().optional(),
	})
