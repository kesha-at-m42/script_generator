extends SequenceEvent

func trigger() -> void:
	var frac_bar = get_frac_shape()
	for part in frac_bar._parts:
		use_label_fraction_tool(part, true)
		use_highlight_tool(part, true)
	use_choice_tool(workspace.validator.answer)
