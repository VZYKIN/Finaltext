from sys import argv # for cli arguments

try:
    sequence_path = argv[1] # Read cli argument
    primer_path = argv[2]
    result_path = argv[3]
    
except:
    raise Exception('No argument given')

try:
    with open(sequence_path, 'r', encoding='utf-8') as sequence: # open seq
        sequence_text = sequence.read()
        with open(primer_path, 'r', encoding='utf-8') as primer: # open prim
            primer_text = primer.read()
            result_text = sequence_text.replace(primer_text, '')
            with open(result_path, 'w', encoding='utf-8') as result: # open res
                print(result_text, file = result)

except:
    raise Exception('Wrong path')
