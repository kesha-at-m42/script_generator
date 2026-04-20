extends SequenceEvent

func trigger() -> void:
	clear_selected()
	
	var frac_bar = get_frac_shape()
	for i in range(frac_bar._parts.size()):
		await delay(0.2)
		use_write_tool(frac_bar._parts[i], str(i + 1))
	await delay(0.2)
	use_highlight_tool(frac_bar._parts[0], true)
