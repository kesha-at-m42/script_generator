extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	for part in bar._parts:
		use_label_fraction_tool(part, true)
	use_choice_tool(workspace.validator.answer)
