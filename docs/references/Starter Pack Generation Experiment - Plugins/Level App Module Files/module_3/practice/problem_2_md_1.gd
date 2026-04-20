extends SequenceEvent

func trigger() -> void:
	for part in get_frac_shape()._parts:
		use_highlight_tool(part, true)
