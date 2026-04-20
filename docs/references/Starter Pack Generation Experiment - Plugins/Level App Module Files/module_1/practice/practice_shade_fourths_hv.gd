extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape()
	clear_shaded(frac_bar)
	use_paint_tool(frac_bar._parts[0])
