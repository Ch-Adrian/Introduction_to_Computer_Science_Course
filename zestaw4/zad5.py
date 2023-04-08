end = None

T = [(-4,4), (-4,0), (0,4), (-2, 0), (0, 2), (0,0)]

def kwadrat(dane):
	"""
	i - lewy górny
	j - prawy górny
	k - prawy dolny
	l - lewy dolny
	"""

	N= len(dane)

	# szukamy lewego górnego
	for i in range(N):

		#szukamy prawego górnego
		for j in range(N):
			znaleziony = True

			# j nie może być poprzednim punktem, y muszą być równe oraz trzeb zapewnić by j leżał po prawej stronie
			if i != j and T[i][1] == T[j][1] and T[j][0] > T[i][0]:

				#szukamy pprawego dolnego
				for k in range(N):
					if k != i and k != j and T[k][0] == T[j][0] and T[k][1] == (T[i][1] - (T[j][0] - T[i][0])):
						
						# szukamy ostatniego
						for l in range(N):
							if l != i and l != j and l != k:
								if T[l][0] == T[i][0] and T[l][1] == T[k][1]:
									
									# sprawdzamy czy nie ma żadnego punktu w środku
									for m in range(N):
										if m != i and m != j and m != k and m != l:
											if T[i][0] <= T[m][0] <= T[k][0] and T[i][1] >= T[m][1] >= T[k][1]:
												znaleziony = False
												break
											end
										end
									end
									if not znaleziony:
										break
									else:
										return True, i, j, k, l
									end
								end
							end
						end
						if not znaleziony:
							break
						end
					end
				end
			end
		end
	end
	return False
end

print(kwadrat(T))