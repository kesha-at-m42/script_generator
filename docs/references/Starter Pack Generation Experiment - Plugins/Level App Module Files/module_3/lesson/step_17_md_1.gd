extends SequenceEvent

func trigger():
	use_highlight_tool(get_frac_shape()._parts.filter(func(frac): return not frac.is_shaded)[0], true)