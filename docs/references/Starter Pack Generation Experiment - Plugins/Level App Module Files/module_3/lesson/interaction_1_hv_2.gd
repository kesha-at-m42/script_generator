extends SequenceEvent

func trigger() -> void:
	var part = get_frac_shape_part(1, 1)
	use_paint_tool(part)
	use_write_tool(part, "2")
