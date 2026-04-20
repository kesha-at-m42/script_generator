extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape(2)
	clear_shaded(frac_bar)
	use_paint_tool(frac_bar._parts[0])
