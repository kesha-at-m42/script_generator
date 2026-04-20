extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	if bar._parts[0].is_shaded:
		use_write_tool(bar._parts[0], "1")
		use_write_tool(bar._parts[1], "2")
	else:
		use_write_tool(bar._parts[0], "2")
		use_write_tool(bar._parts[1], "1")
