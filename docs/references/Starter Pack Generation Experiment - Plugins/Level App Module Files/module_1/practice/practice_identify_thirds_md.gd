extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_selected_frac_shape()
	var bars = get_frac_shapes()
	clear_selected()
	if is_uneven(frac_bar):
		use_comp_frame_tool(get_smallest_part(frac_bar), get_largest_part(frac_bar))
	else:
		use_write_tool_on_bar(frac_bar, func(_part: Fraction, i: int): return str(i + 1))
