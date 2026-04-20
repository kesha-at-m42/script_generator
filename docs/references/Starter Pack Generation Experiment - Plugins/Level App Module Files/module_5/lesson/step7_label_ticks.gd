extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	for i in range(1, 4):
		use_label_fraction_tool(number_line._ticks[i])
		await delay(0.5)
