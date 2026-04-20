extends SequenceEvent

func trigger() -> void:
	var frac_bar = get_number_line().bar
	use_comp_frame_tool(frac_bar._parts[0], frac_bar._parts[1])
	await delay(1)
	use_choice_tool([1])
