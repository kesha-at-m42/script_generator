extends SequenceEvent

func trigger() -> void:
	var selected_frac_bar := get_selected_frac_shape()
	clear_selected()
	#selected bar with two parts instead of three
	if selected_frac_bar == get_frac_shape(0):
		for i in range(selected_frac_bar._parts.size()):
			use_write_tool(selected_frac_bar._parts[i], var_to_str(i + 1))
		await delay(2)
		for i in range(selected_frac_bar._parts.size()):
			use_write_tool(selected_frac_bar._parts[i], "")
	#answer was wrong so must've  selected uneven bar
	else:
		var smallest_part := get_smallest_part(selected_frac_bar)
		var largest_part := get_largest_part(selected_frac_bar)

		use_comp_frame_tool(smallest_part, largest_part)
