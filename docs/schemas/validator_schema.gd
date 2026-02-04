# Copyright Mission 42 Ventures, Inc. All rights reserved.
# Unauthorized copying, distribution, or use is prohibited.

class_name ValidatorSchema extends Node

static var J := JSONSchema

static func create_schema() -> JSONSchema.BaseSchema:
	return J.one_of([
		equal_shaded(),
		shaded_parts(),
		fraction_shape_parts(),
		selection(),
		multiple_choice(),
		tick(),
		point(),
		move(),
		shaded(),
		label(),
		same_shaded()
	])

# ============================================================================
# VALIDATORS
# ============================================================================

static var TYPE_EQUAL_SHADED: String = "fraction_shading"
static var TYPE_SHADED_PARTS: String = "fraction_shaded_parts"
static var TYPE_FRACTION_SHAPE_PARTS: String = "fraction_parts"
static var TYPE_SELECTION: String = "tangible_selection"
static var TYPE_MULTIPLE_CHOICE: String = "multiple_choice"
static var TYPE_SELECT_TICKS: String = "select_ticks"
static var TYPE_PLACE_TICKS: String = "place_ticks"

static func equal_shaded() -> JSONSchema.BaseSchema:
	var schema = J.object({
		# The fraction representing the proportion of parts that each shape should be shaded
		"answer": WorkspaceSchema.fraction().optional()
	})

	schema.deserializer(func(value: Dictionary):
		var new_shaded_validator := ShadedValidator.new()
		new_shaded_validator.answer = value["answer"]
		return new_shaded_validator
	)

	return schema.type(EqualShadedValidator)

static func shaded() -> JSONSchema.BaseSchema:
	return J.object({"answer": WorkspaceSchema.fraction()}).type(ShadedValidator)

static func same_shaded() -> JSONSchema.BaseSchema:
	return J.object({}).type(SameShadedValidator)

static func label() -> JSONSchema.BaseSchema:
	return J.object({"answer": J.array(WorkspaceSchema.fraction())}).type(LabelValidator)

static func shaded_parts() -> JSONSchema.BaseSchema:
	var schema = J.object({
		# The number of parts that should be shaded
		"answer": J.integer().min(0).optional()
	})

	return schema.type(ShadedPartsValidator)

static func fraction_shape_parts() -> JSONSchema.BaseSchema:
	var schema = J.object({
		# The fraction parts representation each fraction shape should match
		"answer": WorkspaceSchema.fraction()
	})

	schema.deserializer(func(value: Dictionary):
		var new_tick_validator := TickValidator.new()
		new_tick_validator.answer = value["answer"]
		return new_tick_validator
	)

	return schema.type(FractionShapePartsValidator)

static func selection() -> JSONSchema.BaseSchema:
	var schema = J.object({
		# The index of the tangible that should be selected
		"answer": J.one_of([J.integer(), J.array(J.integer())])
	})

	return schema.type(SelectionValidator)

static func multiple_choice() -> JSONSchema.BaseSchema:
	var schema = J.object({
		# Array of indices for which options should be selected
		"answer": J.array(J.integer().min(0))
	})

	return schema.type(MultipleChoiceValidator)

static func tick() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"answer": J.one_of([WorkspaceSchema.fraction(), J.array(WorkspaceSchema.fraction())])
	}).type(TickValidator)

	schema.deserializer(func(value: Dictionary) -> TickValidator:
		var new_tick_validator := TickValidator.new()
		var answer = value.get("answer")
		if answer is Array:
			answer.sort_custom(func(a, b):return FracUtils.compare(a.numerator, a.denominator, b.numerator, b.denominator))
		new_tick_validator.answer = answer
		return new_tick_validator
	)

	return schema

static func point() -> JSONSchema.BaseSchema:
	return J.object({"answer": J.array(WorkspaceSchema.fraction())}).type(PointValidator)

static func move() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"answer":  J.array(WorkspaceSchema.fraction())
	})

	schema.deserializer(func(value: Dictionary):
		var new_label_validator := LabelValidator.new()
		new_label_validator.answer = value["answer"]
		return new_label_validator
	)

	return schema.type(MoveValidator)
