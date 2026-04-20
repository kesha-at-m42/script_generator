extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	clear_selected()
	use_comp_frame_tool(bars[1]._parts[0], bars[0]._parts[0])
