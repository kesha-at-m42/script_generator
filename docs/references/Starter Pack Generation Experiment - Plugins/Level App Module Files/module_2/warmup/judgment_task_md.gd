extends SequenceEvent

func trigger() -> void:
	var frac_bars = get_frac_shapes()
	clear_selected()
	var previous_part: Fraction = null
	var current_part: Fraction = null
	for frac_bar in frac_bars:
		previous_part = current_part
		current_part = frac_bar._parts[0]
		if previous_part and current_part:
			use_comp_frame_tool(previous_part, current_part)
			await delay(1)
	await delay(0.5)
