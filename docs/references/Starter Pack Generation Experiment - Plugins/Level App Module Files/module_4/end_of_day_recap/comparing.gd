extends SequenceEvent

func trigger() -> void:
	var lines = get_number_lines()
	use_comp_frame_tool(lines[0].bar._parts[0], lines[1].bar._parts[0])
	await delay(1)
	use_comp_frame_tool(lines[1].bar._parts[0], lines[2].bar._parts[0])
