extends SequenceEvent

func trigger():
	clear_shaded(get_frac_shape())
	use_paint_tool(get_frac_shape_part())