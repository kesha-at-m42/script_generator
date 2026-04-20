extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	use_highlight_tool(bar._parts[0], true)
