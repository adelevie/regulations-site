from django.http import HttpRequest

#   Don't import PartialInterpView directly; this will cause an import cycle
from regulations import views
from regulations.generator.node_types import to_markup_id


class InterpretationsLayer(object):
    """Fetches the (rendered) interpretation for this node, if available"""
    def __init__(self, layer, version=None):
        self.layer = layer
        self.version = version

    def apply_layer(self, text_index):
        """Return a pair of field-name + interpretation if one applies."""
        if text_index in self.layer and self.layer[text_index]:
            layer_element = self.layer[text_index][0]
            reference = layer_element['reference']

            partial_view = views.partial.PartialInterpView.as_view(inline=True)
            request = HttpRequest()
            request.method = 'GET'
            response = partial_view(request, label_id=reference,
                                    version=self.version)
            response.render()

            context = {
                'markup': response.content,
                'for_markup_id': text_index
            }

            #  exclude 'Interp'
            ref_parts = reference.split('-')[:-1]

            if len(ref_parts) == 2:
                #  Part-Section/Appendix
                context['label'] = ref_parts[1]
            elif ref_parts[1].isalpha():
                #  Part-Appendix-Segment
                context['label'] = '-'.join(ref_parts[1:])
            else:
                #  Part-Section-Paragraphs
                context['label'] = (ref_parts[1] + '('
                                    + ')('.join(ref_parts[2:]) + ')')

            return 'interp', context
