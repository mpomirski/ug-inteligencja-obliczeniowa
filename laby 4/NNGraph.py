from graphviz import Digraph
from sklearn.neural_network import MLPClassifier
from typing import List
import math
class NNGraph:
    def __init__(self, model: MLPClassifier, name: str, labels: List[str], input_names: List[str]) -> None:
        self.dot = Digraph(engine='neato')
        self.dot.attr(rankdir='LR', size='16,10', nodesep='2', ranksep='2', splines='false', dim='3', overlap='false', pad='0.5,0.5')
        self.name = name
        self.labels = labels
        self.model = model
        self.input_names = input_names

    def _calculate_spacing(self, elements: int) -> float:
        input_names = 'xzyv'
        input_size = len(input_names)-1
        if elements == 1:
            return input_size/2
        if elements % 2 == 0:
            return (input_size - elements)+0.5 if len(input_names) % 2 == 1 else (input_size - elements)
        return (input_size+1 - elements) / 2

    def _calculate_position(self, elements: int) -> List[float]:
        spacing = [self._calculate_spacing(elements)+i for i in range(elements)]
        return [element -min(spacing)//2 if elements % 2 == 0 and min(spacing) < 0 else element for element in spacing]

    def _calculate_stroke_weight(self, weight: float) -> float:
        return math.log(abs(weight) + 1)+0.25
    
    def _calculate_graph(self) -> None:
        for i, input in enumerate(self.input_names):
            self.dot.node(f'0{i}', input, group='inputs', pos=f'-1,{i}!')
        biases = self.model.intercepts_

        for layer_no, layer in enumerate(self.model.coefs_):
            for i, neuron in enumerate(layer.T):
                if layer_no == len(self.model.coefs_) - 1:
                    self.dot.node(f'{str(layer_no+1) + str(i)}', f'{self.labels[i]}', pos=f'{(len(self.model.coefs_)*10)},{i+0.5}!', group='outputs')
                else:
                    self.dot.node(f'{str(layer_no+1) + str(i)}', f'Neuron {layer_no+1}{i}', pos=f'{(layer_no+2)*4+5},{self._calculate_position(len(layer.T))[i]}!')
                for j, weight in enumerate(neuron):
                    stroke_weight = self._calculate_stroke_weight(weight)
                    self.dot.edge(f'{str(layer_no) + str(j)}', f'{str(layer_no + 1) + str(i)}', xlabel=f'{weight:.2f}', fontsize='6!', fontcolor='blue' if weight > 0 else 'red', penwidth=str(stroke_weight), color='blue' if weight > 0 else 'red')

        # TODO: Implement drawing biases
        # for i, layer in enumerate(biases):
        #     for j, bias in enumerate(layer):
        #         raise NotImplementedError('This method is not implemented yet')
    def draw_graph(self):
        self._calculate_graph()
        self.dot.render(self.name, format='png', cleanup=True)