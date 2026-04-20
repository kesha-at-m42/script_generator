extends SequenceEvent

func trigger() -> void:
	use_comp_frame_tool(get_frac_shape(0)._parts[0], get_frac_shape(1)._parts[0])
