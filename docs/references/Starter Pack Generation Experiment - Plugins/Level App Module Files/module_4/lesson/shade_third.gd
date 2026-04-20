extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	use_paint_tool(bar._parts[0])
