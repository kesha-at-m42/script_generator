extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	use_label_fraction_tool(bar._parts[0], true)
	use_label_fraction_tool(bar._parts[1], true)

	use_choice_tool(workspace.validator.answer)
