extends SequenceEvent

func trigger() -> void:
	use_comp_frame_tool(get_frac_shape(0)._parts[0], get_frac_shape(2)._parts[0])
