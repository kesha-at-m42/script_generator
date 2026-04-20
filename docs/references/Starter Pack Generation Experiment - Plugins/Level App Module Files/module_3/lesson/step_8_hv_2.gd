extends SequenceEvent

func trigger():
	use_paint_tool(get_frac_shape_part(0, 1))
	for part in get_frac_shape()._parts:
		if part.is_shaded:
			part.is_read_only = true
