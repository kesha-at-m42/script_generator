extends SequenceEvent

func trigger() -> void:
	var selected_frac_bar := get_selected_frac_shape()
	var smallest_part := get_smallest_part(selected_frac_bar)
	var largest_part := get_largest_part(selected_frac_bar)

	use_comp_frame_tool(smallest_part, largest_part)
	await delay(2)
	var bars = get_frac_shapes()
	clear_selected()
