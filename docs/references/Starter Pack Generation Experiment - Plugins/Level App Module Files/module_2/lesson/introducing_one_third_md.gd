extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	for i in range(bar._parts.size()):
		use_write_tool(bar._parts[i], var_to_str(i+1))
		await delay(1)
		use_write_tool(bar._parts[i], "")
