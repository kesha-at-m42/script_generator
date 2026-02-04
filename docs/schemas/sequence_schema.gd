class_name SequenceSchema extends Node

static var J := JSONSchema

static func create_schema() -> JSONSchema.BaseSchema:
	return J.object({
		"metadata": metadata().optional(),
		"steps": J.array(step())
	}).type(Sequence)

# ============================================================================
# STEP
# ============================================================================

static func metadata() -> JSONSchema.BaseSchema:
	return J.object({
		"mastery_tier": J.string().enumeration(SequenceMetadata.EMasteryTiers).optional(),
		"mastery_component": J.string().enumeration(SequenceMetadata.EMasteryComponents).optional(),
		"mastery_verbs": J.array(J.string().enumeration(SequenceMetadata.EMasteryVerbs)).optional()
	}).keep_extra_fields_in("unvalidated").type(SequenceMetadata)

static func partial_step() -> JSONSchema.BaseSchema:
	return J.object({
		"metadata": J.dictionary(J.any()).optional(),
		"dialogue": J.string().optional(),
		"audio_dir": J.string().optional(),
	}).type(Step)

static func step() -> JSONSchema.BaseSchema:
	return partial_step().extend({
		"workspace": WorkspaceSchema.create_schema().optional(),
		"prompt": prompt().optional(),
		"scene": J.string().enumeration(ClassroomStore.Scene, ClassroomStore.Scene.None).optional(),
		"pool": PoolSchema.create_schema().optional()
	})

static func prompt() -> JSONSchema.BaseSchema:
	var schema = J.object({
		"text": J.string(),
		"tool": ToolSchema.create_schema().optional(),
		"validator": ValidatorSchema.create_schema().optional(),
		"choices": choices().optional(),
		"palette": PaletteSchema.create_schema().optional(),
		"remediations": J.array(remediation()).optional(),
		"on_correct": partial_step().optional(),
	}).type(Prompt)

	schema.deserializer(func(value : Dictionary) -> Prompt:
		var new_prompt := Prompt.new()

		new_prompt.text = value.text

		if "tool" in value:
			if value.tool is Move:
				var move := value.tool as Move

				if "palette" in value and not move.palette:
					# Migrate Prompt-based Palette information to the Move Tool, if it exists.
					move.palette = value.palette

				new_prompt.tool = move
			else:
				new_prompt.tool = value.tool

		if "validator" in value:
			new_prompt.validator = value.validator
		if "choices" in value:
			new_prompt.choices = value.choices
		if "remediations" in value:
			new_prompt.remediations.append_array(value.remediations)
		if "on_correct" in value:
			new_prompt.on_correct = value.on_correct

		return new_prompt
	)

	return schema

static func choices() -> JSONSchema.BaseSchema:
	var schema := J.object({
		"allow_multiple": J.boolean().optional(),
		"options": J.array(J.string())
	}).type(WorkspaceChoices)

	schema.serializer(func(value: WorkspaceChoices) -> Variant:
		if value.options.size() == 0:
			return null
		return value
	)

	return schema

static func remediation() -> JSONSchema.BaseSchema:
	return J.object({
		"id": J.string(),
		"step": partial_step()
	}).type(Remediation)
