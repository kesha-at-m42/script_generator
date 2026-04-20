extends SequenceEvent

func trigger() -> void:
	#style - this remediation uses 'one-sixth' instead of 1/6 mod 2 exit check 4 also AI

	clear_shaded(get_frac_shape())
	use_paint_tool(get_frac_shape_part(0,0))
