/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Layout } from "@web/views/layout";
import { KeepLast } from "@web/core/utils/concurrency";
import { Model, useModel } from "@web/views/helpers/model";

class VeryBasicModel extends Model {
  static services = ["orm"];

  setup(params, { orm }) {
    this.model = params.resModel;
    this.orm = orm;
    this.keepLast = new KeepLast();
  }

  async load(params) {
    this.data = await this.keepLast.add(
      this.orm.searchRead(this.model, params.domain, [], { limit: 100 })
    );
    this.notify();
  }
}
VeryBasicModel.services = ["orm"];

class VeryBasicView extends owl.Component {
  setup() {
    this.model = useModel(VeryBasicModel, {
      resModel: this.props.resModel,
      domain: this.props.domain,
    });
  }
}

VeryBasicView.type = "very_basic_view";
VeryBasicView.display_name = "VeryBasicView";
VeryBasicView.icon = "fa-heart";
VeryBasicView.multiRecord = true;
VeryBasicView.searchMenuTypes = ["filter", "favorite"];
VeryBasicView.components = { Layout };
VeryBasicView.template = owl.tags.xml/* xml */ `
<Layout viewType="'very_basic_view'">
    <div><h1>Hello OwlView</h1></div>
    <div t-foreach="model.data" t-as="record" t-key="record.id">
        <t t-esc="record.name"/>
    </div>
</Layout>`;

registry.category("views").add("very_basic_view", VeryBasicView);
