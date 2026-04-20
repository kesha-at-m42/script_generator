extends SequenceEvent

func trigger() -> void:
	clear_shaded(get_frac_shape(1))
	var part := get_frac_shape_part(1, 0)
	part.is_shaded = true
	use_highlight_tool(part, true)
	use_write_tool(part, "1")
