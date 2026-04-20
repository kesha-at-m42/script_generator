extends SequenceEvent

func trigger() -> void:
	clear_selected()
	use_comp_frame_tool(bars[0]._parts[0], bars[1]._parts[0])
	await delay(2)
	use_comp_frame_tool(bars[0]._parts[0], bars[2]._parts[0])
