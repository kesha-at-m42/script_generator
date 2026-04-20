extends SequenceEvent

func trigger() -> void:
	var bars = get_frac_shapes()
	clear_selected()
	for bar in bars:
		use_select_tool(bar)
		await delay(1)
