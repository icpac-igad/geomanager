from rest_framework import serializers

from geomanager.models import TmsLayer


class TmsLayerSerializer(serializers.ModelSerializer):
    layerConfig = serializers.SerializerMethodField()
    params = serializers.SerializerMethodField()
    paramsSelectorConfig = serializers.SerializerMethodField()
    legendConfig = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    layerType = serializers.SerializerMethodField()
    multiTemporal = serializers.SerializerMethodField()
    currentTimeMethod = serializers.SerializerMethodField()
    paramsSelectorColumnView = serializers.SerializerMethodField()
    autoUpdateInterval = serializers.SerializerMethodField()
    isMultiLayer = serializers.SerializerMethodField()
    nestedLegend = serializers.SerializerMethodField()
    moreInfo = serializers.SerializerMethodField()

    class Meta:
        model = TmsLayer
        fields = ["id", "dataset", "name", "isMultiLayer", "nestedLegend", "layerType", "layerConfig", "params",
                  "paramsSelectorConfig", "paramsSelectorColumnView", "legendConfig", "multiTemporal",
                  "currentTimeMethod", "autoUpdateInterval", "moreInfo", ]

    def get_isMultiLayer(self, obj):
        return obj.dataset.multi_layer

    def get_nestedLegend(self, obj):
        return obj.dataset.multi_layer

    def get_autoUpdateInterval(self, obj):
        return obj.dataset.auto_update_interval_milliseconds

    def get_multiTemporal(self, obj):
        return obj.dataset.multi_temporal

    def get_currentTimeMethod(self, obj):
        return obj.dataset.current_time_method

    def get_layerType(self, obj):
        return obj.dataset.layer_type

    def get_name(self, obj):
        return obj.title

    def get_layerConfig(self, obj):
        layer_config = obj.layer_config

        return layer_config

    def get_params(self, obj):
        return obj.params

    def get_paramsSelectorConfig(self, obj):
        return obj.param_selector_config

    def get_paramsSelectorColumnView(self, obj):
        return not obj.params_selectors_side_by_side

    def get_legendConfig(self, obj):
        request = self.context.get('request')
        return obj.get_legend_config(request)

    def get_moreInfo(self, obj):
        info = None
        for info in obj.more_info:
            info = info.value.as_dict
        return info
