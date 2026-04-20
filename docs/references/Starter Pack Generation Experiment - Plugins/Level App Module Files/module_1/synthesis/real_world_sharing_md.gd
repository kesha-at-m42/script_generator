extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	clear_selected()
	use_comp_frame_tool(get_frac_shape(0)._parts[0], get_frac_shape(1)._parts[0])
	await delay(1.5)
	use_comp_frame_tool(get_frac_shape(1)._parts[0], get_frac_shape(2)._parts[0])
