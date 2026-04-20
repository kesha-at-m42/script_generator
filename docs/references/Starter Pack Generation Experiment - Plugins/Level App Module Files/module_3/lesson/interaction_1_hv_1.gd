extends SequenceEvent

func trigger() -> void:
	clear_shaded(get_frac_shape(1))
	var part = get_frac_shape_part(1, 0)
	use_paint_tool(part)
	use_write_tool(part, "1")
