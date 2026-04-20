extends SequenceEvent

func trigger() -> void:
	use_highlight_tool(get_frac_shape()._parts[0], true)
