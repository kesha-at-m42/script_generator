extends SequenceEvent

func trigger() -> void:
	var part := get_frac_shape_part(1, 1)
	use_highlight_tool(part, true)
	use_write_tool(part, "2")
