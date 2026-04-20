extends SequenceEvent

func trigger() -> void:
	var frac_bars := get_frac_shapes()
	for frac_bar in frac_bars:
		if is_uneven(frac_bar):
			use_comp_frame_tool(get_smallest_part(frac_bar), get_largest_part(frac_bar))
			await delay(1.5)
