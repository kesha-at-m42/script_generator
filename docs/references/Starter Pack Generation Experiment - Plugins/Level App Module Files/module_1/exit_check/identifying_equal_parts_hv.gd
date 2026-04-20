extends SequenceEvent

func trigger() -> void:
	clear_selected()
	var correct_bar := get_frac_shape(1)
	use_select_tool(correct_bar)
	use_comp_frame_tool(correct_bar._parts[0], correct_bar._parts[1])
	await delay(2)
	use_comp_frame_tool(correct_bar._parts[1], correct_bar._parts[2])
