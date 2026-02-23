"""
C4 Level 2 — Container diagram (diagrams as code).
Translated from PlantUML c4-l2-containers.
"""
from diagrams import Diagram, Cluster
from diagrams.c4 import Container
from diagrams.generic.blank import Blank

_DASH = {"style": "dashed"}

with Diagram(
    "C4 L2 — Containers",
    direction="TB",
    show=False,
    filename="c4-l2-containers",
    graph_attr={"splines": "spline", "compound": "true"},
    node_attr={"fontsize": "8", "margin": "0.25"},
):
    with Cluster("Shared (Cloud or On-Prem)", graph_attr=_DASH):
        with Cluster("External integrations", graph_attr=_DASH):
            ext_dns = Blank("DNS & CDN\nProvider API")
            ext_games = Blank("Games\nProvider API")
            ext_pay = Blank("Payments\nProvider API")
            ext_fraud = Blank("Fraud Detection\nProvider API")
            ext_kyc = Blank("KYC\nProvider API")
            ext_aml = Blank("AML\nProvider API")
            ext_cs = Blank("Customer Support\nProvider API")

        with Cluster("Self-hosted Services", graph_attr=_DASH):
            with Cluster("Secrets", graph_attr=_DASH):
                with Cluster("Core", graph_attr=_DASH):
                    shared_secrets_core_service = Container(
                        "Shared Secrets Core\n\n(Hashicorp Vault)", "", ""
                    )
            with Cluster("Container Registry", graph_attr=_DASH):
                with Cluster("Core", graph_attr=_DASH):
                    shared_container_registry_core_service = Container(
                        "Shared Container Registry\nCore (Managed Cloud)", "", ""
                    )
            with Cluster("Registry", graph_attr=_DASH):
                with Cluster("Core", graph_attr=_DASH):
                    shared_registry_core_service = Container(
                        "Shared Registry Core\n(Nexus)", "", ""
                    )
            with Cluster("Observability", graph_attr=_DASH):
                with Cluster("Core", graph_attr=_DASH):
                    shared_observability_core_service = Container(
                        "Shared Observability Core\n(Grafana)", "", ""
                    )

    with Cluster("Environment", graph_attr=_DASH):
        with Cluster("Product Instance (B2B2C Gambling Platform)", graph_attr=_DASH):
            env_node = Blank("Environment")

            with Cluster("Platform Cluster (k8s)", graph_attr=_DASH):
                with Cluster("Platform", graph_attr=_DASH):
                    with Cluster("Gateway", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_gateway_core_service = Container(
                                "Platform Gateway Core \n(Traefik)", "", ""
                            )
                    with Cluster("Events", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_events_core_service = Container(
                                "Platform Events Core \n(Argo Events)", "", ""
                            )
                        with Cluster("Webhooks", graph_attr=_DASH):
                            plat_events_webhooks_service = Container(
                                "Platform Events Webhooks \n(Argo Events)", "", ""
                            )
                    with Cluster("CI", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_ci_core_service = Container(
                                "Platform CI Core \n(Argo Workflows)", "", ""
                            )
                        with Cluster("Pipelines", graph_attr=_DASH):
                            plat_ci_pipelines_service = Container(
                                "Platform CI Pipelines \n(Argo Workflows)", "", ""
                            )
                    with Cluster("CD", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_cd_core_service = Container(
                                "Platform CD Core \n(ArgoCD)", "", ""
                            )
                    with Cluster("Image-updater", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_imgupd_core_service = Container(
                                "Platform Image-updater Core \n(Argo Image Updater)", "", ""
                            )
                    with Cluster("SMTP", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_smtp_core_service = Container(
                                "Platform SMTP Core \n(Mailu)", "", ""
                            )
                    with Cluster("Images", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_images_core_service = Container(
                                "Platform Images Core \n(imgProxy)", "", ""
                            )
                    with Cluster("Certificates", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_certs_core_service = Container(
                                "Platform Certificates Core \n(CertManager)", "", ""
                            )
                    with Cluster("Configs", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_configs_core_service = Container(
                                "Platform Configs Core \n(OpenFeature Flags)", "", ""
                            )
                    with Cluster("Secrets", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_secrets_core_service = Container(
                                "Platform Secrets Core \n(Hashicorp Vault)", "", ""
                            )
                    with Cluster("Metrics", graph_attr=_DASH):
                        with Cluster("Hub", graph_attr=_DASH):
                            plat_metrics_hub_service = Container(
                                "Platform Metrics Hub \n(vmagent)", "", ""
                            )
                        with Cluster("K3s", graph_attr=_DASH):
                            plat_metrics_k3s_service = Container(
                                "Platform Metrics K3s \n(metrics-server)", "", ""
                            )
                        with Cluster("OS", graph_attr=_DASH):
                            plat_metrics_os_service = Container(
                                "Platform Metrics OS \n(node_exporter)", "", ""
                            )
                    with Cluster("Logs", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_logs_core_service = Container(
                                "Platform Logs Core \n(Promtail)", "", ""
                            )
                    with Cluster("Traces", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_traces_core_service = Container(
                                "Platform Traces Core \n(Tempo)", "", ""
                            )
                    with Cluster("Errors", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_errors_core_service = Container(
                                "Platform Errors Core \n(Sentry)", "", ""
                            )
                    with Cluster("Profiles", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_profiles_core_service = Container(
                                "Platform Profiles Core \n(Grafana Alloy)", "", ""
                            )
                    with Cluster("Collector", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_collector_core_service = Container(
                                "Platform Collector Core \n(OTel Collector)", "", ""
                            )
                    with Cluster("Operator", graph_attr=_DASH):
                        with Cluster("Integration", graph_attr=_DASH):
                            plat_operator_integration_service = Container(
                                "Platform Operator Integration \n(MirrorMaker2)", "", ""
                            )
                    with Cluster("Casino", graph_attr=_DASH):
                        with Cluster("Integration", graph_attr=_DASH):
                            plat_casino_integration_service = Container(
                                "Platform Casino Integration \n(MirrorMaker2)", "", ""
                            )
                    with Cluster("Bus", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            plat_bus_core_service = Container(
                                "Platform Bus Core \n(Kafka)", "", ""
                            )
                        with Cluster("Viewer", graph_attr=_DASH):
                            plat_bus_viewer_service = Container(
                                "Platform Bus Viewer \n(kafka-ui)", "", ""
                            )

            with Cluster("B2B SaaS Operator Cluster (k8s)", graph_attr=_DASH):
                with Cluster("Operator", graph_attr=_DASH):
                    with Cluster("Gateway", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            op_gateway_core_service = Container(
                                "Operator Gateway Core \n(Traefik)", "", ""
                            )
                    with Cluster("CRM", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            op_crm_core_webapp = Container(
                                "Operator CRM Core Webapp \n(Next.js)", "", ""
                            )
                            op_crm_core_service = Container(
                                "Operator CRM Core Service \n(Nest.js)", "", ""
                            )
                            op_crm_core_db = Container(
                                "Operator CRM Core DB \n(PostgreSQL)", "", ""
                            )
                    with Cluster("Reports", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            op_reports_core_service = Container(
                                "Operator Reports Core Service \n(Nest.js)", "", ""
                            )
                            op_reports_core_objects = Container(
                                "Operator Reports Core Objects \n(S3)", "", ""
                            )
                            op_reports_core_db = Container(
                                "Operator Reports Core DB \n(PostgreSQL)", "", ""
                            )
                    with Cluster("IAM", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            op_iam_core_service = Container(
                                "Operator IAM Core \n(Keycloak)", "", ""
                            )
                            op_iam_core_db = Container(
                                "Operator IAM Core DB \n(PostgreSQL)", "", ""
                            )
                    with Cluster("Casino", graph_attr=_DASH):
                        with Cluster("Integration", graph_attr=_DASH):
                            op_casino_integration_service = Container(
                                "Operator Casino Integration \n(MirrorMaker2)", "", ""
                            )
                    with Cluster("Bus", graph_attr=_DASH):
                        with Cluster("Core", graph_attr=_DASH):
                            op_bus_core_service = Container(
                                "Operator Bus Core \n(Kafka)", "", ""
                            )
                        with Cluster("Viewer", graph_attr=_DASH):
                            op_bus_viewer_service = Container(
                                "Operator Bus Viewer \n(kafka-ui)", "", ""
                            )

            with Cluster("B2C SaaS Casino Cluster (k8s)", graph_attr=_DASH):
                with Cluster("Gateway", graph_attr=_DASH):
                    with Cluster("Core", graph_attr=_DASH):
                        casino_gateway_core_service = Container(
                            "Casino Gateway Core \n(Traefik)", "", ""
                        )
                with Cluster("Brand", graph_attr=_DASH):
                    with Cluster("Core", graph_attr=_DASH):
                        casino_brand_core_webapp = Container(
                            "Casino Brand Core Webapp \n(Next.js)", "", ""
                        )
                        casino_brand_core_service = Container(
                            "Casino Brand Core Service \n(Nest.js)", "", ""
                        )
                        casino_brand_core_db = Container(
                            "Casino Brand Core DB \n(PostgreSQL)", "", ""
                        )
                        casino_brand_core_sidecar = Container(
                            "Casino Brand Core Sidecar \n(Nest.js)", "", ""
                        )
                        casino_brand_core_cache = Container(
                            "Casino Brand Core Cache \n(Redis)", "", ""
                        )
                with Cluster("IAM", graph_attr=_DASH):
                    with Cluster("Core", graph_attr=_DASH):
                        casino_iam_core_service = Container(
                            "Casino IAM Core \n(Keycloak)", "", ""
                        )
                        casino_iam_core_db = Container(
                            "Casino IAM Core DB \n(PostgreSQL)", "", ""
                        )
                    with Cluster("Sessions", graph_attr=_DASH):
                        casino_iam_sessions_service = Container(
                            "Casino IAM Sessions Service \n(Nest.js)", "", ""
                        )
                        casino_iam_sessions_db = Container(
                            "Casino IAM Sessions DB \n(PostgreSQL)", "", ""
                        )
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_iam_integration_service = Container(
                            "Casino IAM Integration \n(Nest.js)", "", ""
                        )
                with Cluster("CMS", graph_attr=_DASH):
                    with Cluster("Core", graph_attr=_DASH):
                        casino_cms_core_service = Container(
                            "Casino CMS Core \n(Payload)", "", ""
                        )
                        casino_cms_core_db = Container(
                            "Casino CMS Core DB \n(PostgreSQL)", "", ""
                        )
                        casino_cms_core_objects = Container(
                            "Casino CMS Core Objects \n(S3)", "", ""
                        )
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_cms_integration_service = Container(
                            "Casino CMS Integration \n(Nest.js)", "", ""
                        )
                with Cluster("Bus", graph_attr=_DASH):
                    with Cluster("Core", graph_attr=_DASH):
                        casino_bus_core_service = Container(
                            "Casino Bus Core \n(Kafka)", "", ""
                        )
                    with Cluster("Viewer", graph_attr=_DASH):
                        casino_bus_viewer_service = Container(
                            "Casino Bus Viewer \n(kafka-ui)", "", ""
                        )
                with Cluster("KYC", graph_attr=_DASH):
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_kyc_integration_service = Container(
                            "Casino KYC Integration \n(Nest.js)", "", ""
                        )
                with Cluster("AML", graph_attr=_DASH):
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_aml_integration_service = Container(
                            "Casino AML Integration \n(Nest.js)", "", ""
                        )
                with Cluster("Fraud", graph_attr=_DASH):
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_fraud_integration_service = Container(
                            "Casino Fraud Integration \n(Nest.js)", "", ""
                        )
                with Cluster("Games", graph_attr=_DASH):
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_games_integration_service = Container(
                            "Casino Games Integration \n(Nest.js)", "", ""
                        )
                with Cluster("Payments", graph_attr=_DASH):
                    with Cluster("Integration", graph_attr=_DASH):
                        casino_payments_integration_service = Container(
                            "Casino Payments Integration \n(Nest.js)", "", ""
                        )

    # ----- Links: Casino cluster internal -----
    casino_brand_core_service >> casino_brand_core_db
    casino_brand_core_service >> casino_brand_core_cache
    casino_brand_core_service >> casino_brand_core_sidecar
    casino_brand_core_sidecar >> casino_bus_core_service
    casino_gateway_core_service >> casino_brand_core_webapp
    casino_gateway_core_service >> casino_brand_core_service
    casino_gateway_core_service >> casino_cms_core_service
    casino_gateway_core_service >> casino_iam_core_service
    casino_gateway_core_service >> casino_iam_sessions_service
    casino_gateway_core_service >> casino_bus_core_service
    casino_gateway_core_service >> casino_bus_viewer_service
    casino_iam_core_service >> casino_iam_core_db
    casino_iam_sessions_service >> casino_iam_sessions_db
    casino_iam_sessions_service >> casino_bus_core_service
    casino_iam_core_service >> casino_iam_integration_service
    casino_iam_integration_service >> casino_bus_core_service
    casino_cms_core_service >> casino_cms_core_db
    casino_cms_core_service >> casino_cms_core_objects
    casino_cms_integration_service >> casino_bus_core_service
    casino_cms_integration_service >> casino_cms_core_service
    casino_bus_viewer_service << casino_bus_core_service

    # ----- Casino integrations to external and bus -----
    casino_kyc_integration_service >> ext_kyc
    casino_kyc_integration_service >> casino_bus_core_service
    casino_aml_integration_service >> ext_aml
    casino_aml_integration_service >> casino_bus_core_service
    casino_fraud_integration_service >> ext_fraud
    casino_fraud_integration_service >> casino_bus_core_service
    casino_games_integration_service >> ext_games
    casino_games_integration_service >> casino_bus_core_service
    casino_payments_integration_service >> ext_pay
    casino_payments_integration_service >> casino_bus_core_service

    # ----- Operator cluster internal -----
    op_gateway_core_service >> op_crm_core_webapp
    op_gateway_core_service >> op_crm_core_service
    op_gateway_core_service >> op_reports_core_service
    op_gateway_core_service >> op_iam_core_service
    op_gateway_core_service >> op_bus_core_service
    op_gateway_core_service >> op_bus_viewer_service
    op_crm_core_service >> op_crm_core_db
    op_crm_core_service >> op_iam_core_service
    op_crm_core_service >> op_bus_core_service
    op_reports_core_service >> op_reports_core_db
    op_reports_core_service >> op_reports_core_objects
    op_reports_core_service >> op_bus_core_service
    op_reports_core_service >> op_iam_core_service
    op_iam_core_service >> op_iam_core_db
    op_bus_viewer_service << op_bus_core_service
    op_casino_integration_service >> op_bus_core_service
    casino_gateway_core_service << op_casino_integration_service

    # ----- Platform cluster -----
    plat_bus_viewer_service << plat_bus_core_service
    plat_bus_core_service >> plat_operator_integration_service
    op_gateway_core_service >> plat_operator_integration_service
    plat_bus_core_service >> plat_casino_integration_service
    casino_gateway_core_service >> plat_casino_integration_service

    # ----- Platform Gateway to internal services -----
    plat_gateway_core_service >> plat_events_core_service
    plat_gateway_core_service >> plat_events_webhooks_service
    plat_gateway_core_service >> plat_ci_core_service
    plat_gateway_core_service >> plat_ci_pipelines_service
    plat_gateway_core_service >> plat_cd_core_service
    plat_gateway_core_service >> plat_imgupd_core_service
    plat_gateway_core_service >> plat_smtp_core_service
    plat_gateway_core_service >> plat_images_core_service
    plat_gateway_core_service >> plat_configs_core_service
    plat_gateway_core_service >> plat_secrets_core_service
    plat_gateway_core_service >> plat_metrics_hub_service
    plat_gateway_core_service >> plat_logs_core_service
    plat_gateway_core_service >> plat_traces_core_service
    plat_gateway_core_service >> plat_errors_core_service
    plat_gateway_core_service >> plat_profiles_core_service
    plat_gateway_core_service >> plat_certs_core_service
    plat_gateway_core_service >> plat_bus_core_service
    plat_gateway_core_service >> plat_bus_viewer_service
    plat_gateway_core_service >> plat_collector_core_service

    # ----- Shared services to Environment -----
    shared_secrets_core_service >> env_node
    shared_container_registry_core_service >> env_node
    shared_registry_core_service >> env_node
    shared_observability_core_service >> env_node
