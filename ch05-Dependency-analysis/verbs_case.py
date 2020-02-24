# Author：ambiguoustexture
# Date: 2020-02-24

from chunk_analysis import chunk_analysis

file_parsed = './neko.txt.cabocha'
file_result = './verbs_case_result.txt'

with open(file_parsed, 'r') as text_parsed, open(file_result, 'w') as text_result:
    sentences = chunk_analysis(text_parsed)
    
    for sentence in sentences:
        for chunk in sentence:
            verbs = chunk.get_morphs_by_pos('動詞')
            if len(verbs) < 1:
                continue
            particles = []
            for src in chunk.srcs:
                particles_in_chunk = sentence[src].get_morphs_by_pos('助詞')
                if len(particles_in_chunk) > 1:
                    case_particles = sentence[src].get_morphs_by_pos('助詞', '格助詞')
                    if len(case_particles) > 0:
                        particles_in_chunk = case_particles
                if len(particles_in_chunk) > 0:
                    particles.append(particles_in_chunk[-1])
            if len(particles) < 1:
                continue
            text_result.write('{}\t{}\n'\
                    .format(verbs[0].base, ' '.join(sorted(particle.surface for particle in particles))))
