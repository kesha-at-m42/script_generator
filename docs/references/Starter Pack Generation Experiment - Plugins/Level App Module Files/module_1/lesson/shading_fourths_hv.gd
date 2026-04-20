extends SequenceEvent

func trigger() -> void:
	clear_shaded(get_frac_shape())
	use_paint_tool(get_frac_shape()._parts[0])
