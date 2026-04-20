extends SequenceEvent

func trigger():
	var bars := get_frac_shapes()
	clear_selected()
	for bar in bars:
		for part in get_shaded_parts():
			use_highlight_tool(part, true)
			await delay(0.2)
		await delay(1)
		clear_highlights(bar)
