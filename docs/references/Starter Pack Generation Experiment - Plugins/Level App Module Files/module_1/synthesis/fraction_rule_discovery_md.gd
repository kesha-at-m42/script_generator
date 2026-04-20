extends SequenceEvent

func trigger() -> void:
	for frac_bar in get_frac_shapes():
		var previous_part: Fraction = null
		var current_part: Fraction = null
		for frac_bar_part in frac_bar._parts:
			previous_part = current_part
			current_part = frac_bar_part
			if previous_part and current_part and previous_part.numeric() <= current_part.numeric():
				use_comp_frame_tool(previous_part, current_part)
				await delay(0.75)
		await delay(0.25)
