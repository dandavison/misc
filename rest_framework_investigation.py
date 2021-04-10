from StringIO import StringIO

from rest_framework import renderers
from rest_framework import serializers
from rest_framework_csv import renderers as csv_renderers


class Serializer(serializers.Serializer):
    field1 = serializers.IntegerField()
    field2 = serializers.CharField()


class VCFSerializer(serializers.Serializer):
    CHROM = serializers.CharField()
    POS = serializers.IntegerField()
    ID = serializers.CharField()
    REF = serializers.CharField()
    ALT = serializers.CharField()
    QUAL = serializers.FloatField()
    FILTER = serializers.CharField()
    INFO = serializers.CharField()


class VCFFileRenderer(renderers.BaseRenderer):

    def __init__(self, fp, *args, **kwargs):
        super(VCFFileRenderer, self).__init__(*args, **kwargs)
        self.fp = fp

    def render(self, data, **kwargs):
        if isinstance(data, dict):
            data = [data]
        for row in data:
            # FIXME: How does the renderer know how to format different field types?
            self.fp.write('\t'.join(map(str, row.values())) + '\n')


vcf_rows = [
    {'CHROM': 'chr1', 'POS': 22, 'ID': 'rs12345', 'REF': 'A', 'ALT': 'T', 'QUAL': 2.3, 'FILTER': 'PASS', 'INFO': 'k1=v11;k2=v12'},
    {'CHROM': 'chr2', 'POS': 11, 'ID': 'rs67891', 'REF': 'CAG', 'ALT': 'GCC', 'QUAL': 1.3, 'FILTER': 'PASS', 'INFO': 'k1=v21;k2=v22'},
]


serializer = VCFSerializer(vcf_rows, many=True)
buffer = StringIO()
renderer = VCFFileRenderer(buffer)
renderer.render(serializer.data)


def investigate_one_many():
    data = [
        {'field1': 1, 'field2': 'a'},
        {'field1': 2, 'field2': 'b'},
    ]
    renderer = csv_renderers.CSVRenderer()
    serializer = Serializer(data, many=True)

    datum_serializer = Serializer(data[0])
    data_serializer = Serializer(data, many=True)


    datum_serializer.data
    # {'field2': u'a', 'field1': 1}

    data_serializer.data
    # [OrderedDict([('field1', 1), ('field2', u'a')]), OrderedDict([('field1', 2), ('field2', u'b')])]


    print renderer.render(datum_serializer.data)
    # field1,field2
    # 1,a


    print renderer.render(data_serializer.data)
    # field1,field2
    # 1,a
    # 2,b
