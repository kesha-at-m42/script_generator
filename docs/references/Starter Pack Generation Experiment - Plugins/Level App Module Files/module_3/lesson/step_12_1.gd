extends SequenceEvent

func trigger():
	for part in get_frac_shape()._parts.filter(func(frac): return frac.is_shaded):
		use_highlight_tool(part, true)
