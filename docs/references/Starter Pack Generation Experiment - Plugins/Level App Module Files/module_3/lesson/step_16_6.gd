extends SequenceEvent

func trigger():
	var shaded_parts = get_shaded_parts()
	use_paint_tool(shaded_parts[2])
	await delay(0.5)
	use_paint_tool(shaded_parts[1])
	await delay(0.5)
	use_paint_tool(shaded_parts[0])
	await delay(0.5)
	use_paint_tool(shaded_parts[0])
	await delay(0.5)
	use_paint_tool(shaded_parts[1])
	await delay(0.5)
	use_paint_tool(shaded_parts[2])
